from dataclasses import dataclass


@dataclass
class DatasetConfig:
    # Dataset settings
    data_flag: str = "pneumoniamnist"
    root: str = "backend/data/medmnist"
    dataset_size: int = 28

    # Model input settings
    input_size: int = 128
    as_rgb: bool = True
    num_classes: int = 2

    # Small subsets for Loop 1
    train_samples: int = 240
    val_samples: int = 60
    test_samples: int = 60

    # Training settings
    batch_size: int = 16
    epochs: int = 1
    num_workers: int = 0
    seed: int = 42

    # Download settings
    download: bool = True