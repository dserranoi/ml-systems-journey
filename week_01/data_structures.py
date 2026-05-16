from dataclasses import dataclass, field

@dataclass
class TrainingConfig:
    """Configuration for a training run."""
    learning_rate: float
    batch_size: int
    epochs: int
    model_name: str = "baseline"
    tags: list [str] = field(default_factory=list)

    def describe(self) ->str:
        return f"{self.model_name} | lr={self.learning_rate} | batch={self.batch_size}"
if __name__ == "__main__":
    config = TrainingConfig(
        learning_rate=0.001,
        batch_size=32,
        epochs=10,
    )

    print(config)
    print(config.describe())
    print(config.learning_rate)

    # Compare with a plain dict
    config_dict = {
        "learning_rate": 0.001,
        "batch_size": 32,
        "epochs": 10,
    }

    print(config_dict["learning_rate"])
    # config_dict.describe()  # this would crash - dicts have no methods

    # Dataclasses are comparable by default
    config2 = TrainingConfig(
        learning_rate=0.001,
        batch_size=32,
        epochs=10,
    )

    print(config == config2)  # True - compares all fields automatically