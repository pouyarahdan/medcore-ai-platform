from pathlib import Path

import medmnist
import numpy as np
from medmnist import INFO
from torch.utils.data import DataLoader, Subset
from torchvision import transforms

from backend.ai.dataset_config import DatasetConfig


def get_transforms(config):
    return transforms.Compose([
        transforms.Resize(
            (config.input_size, config.input_size)
        ),
        transforms.ToTensor(),
        transforms.Normalize(
            mean=[0.485, 0.456, 0.406],
            std=[0.229, 0.224, 0.225]
        )
    ])


def select_samples(dataset, sample_count, seed):
    labels = dataset.labels.flatten()
    classes = np.unique(labels)

    if len(classes) != 2:
        raise ValueError(
            "Loop 1 supports binary classification only"
        )

    if sample_count < 2 or sample_count % 2 != 0:
        raise ValueError(
            "Sample count must be a positive even number"
        )

    rng = np.random.default_rng(seed)
    samples_per_class = sample_count // 2
    selected_indices = []

    for label in classes:
        class_indices = np.where(labels == label)[0]

        if len(class_indices) < samples_per_class:
            raise ValueError(
                f"Not enough samples for class {label}"
            )

        chosen = rng.choice(
            class_indices,
            size=samples_per_class,
            replace=False
        )

        selected_indices.extend(chosen.tolist())

    rng.shuffle(selected_indices)

    return Subset(dataset, selected_indices)


def build_dataloaders(config: DatasetConfig):
    Path(config.root).mkdir(
        parents=True,
        exist_ok=True
    )

    info = INFO[config.data_flag]
    dataset_class = getattr(
        medmnist,
        info["python_class"]
    )

    if not config.as_rgb:
        raise ValueError(
            "ResNet18 requires 3-channel input"
        )

    transform = get_transforms(config)

    split_settings = [
        ("train", config.train_samples),
        ("val", config.val_samples),
        ("test", config.test_samples)
    ]

    loaders = []

    for index, (split, sample_count) in enumerate(
        split_settings
    ):
        dataset = dataset_class(
            split=split,
            transform=transform,
            download=config.download,
            size=config.dataset_size,
            as_rgb=config.as_rgb,
            root=config.root
        )

        subset = select_samples(
            dataset,
            sample_count,
            config.seed + index
        )

        loader = DataLoader(
            subset,
            batch_size=config.batch_size,
            shuffle=(split == "train"),
            num_workers=config.num_workers
        )

        loaders.append(loader)

    return tuple(loaders)