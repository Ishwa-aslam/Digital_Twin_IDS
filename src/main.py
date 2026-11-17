
import subprocess
import sys
from pathlib import Path

# Project root directory
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Available project modules
modules = {
    "1": ("Digital Twin Simulation", "digital_twin.py"),
    "2": ("Dataset Preparation", "prepare_dataset.py"),
    "3": ("Data Visualization", "plot_data.py"),
    "4": ("Exploratory Data Analysis", "eda.py"),
    "5": ("Data Preprocessing", "preprocessing.py"),
    "6": ("ML Model Training", "train_models.py"),
    "7": ("Feature Group Experiment (E4)", "feature_experiment.py"),
    "8": ("Resource Experiment (E5)", "resource_experiment.py"),
    "9": ("Robustness Experiment (E6)", "robustness_experiment.py"),
    "10": ("OS Monitoring", "os_monitor.py"),
    "11": ("OS Concepts Demonstration", "os_concepts.py"),
    "12": ("CPU Scheduling Simulation", "cpu_scheduling.py")
}


def run_module(name, filename):
    print(f"\nStarting: {name}")
    print("-" * 45)

    script_path = PROJECT_ROOT / "src" / filename

    result = subprocess.run(
        [sys.executable, str(script_path)],
        cwd=PROJECT_ROOT
    )

    if result.returncode == 0:
        print(f"\n{name} completed successfully!")
    else:
        print(f"\nError while running {name}!")

    return result.returncode


def main():
    print("=" * 50)
    print(" DIGITAL TWIN-BASED INTRUSION DETECTION SYSTEM")
    print("=" * 50)

    while True:
        print("\nPROJECT MENU")

        for key, (name, filename) in modules.items():
            print(f"{key}. {name}")

        print("13. Run Complete Project Pipeline")
        print("0. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "0":
            print("\nProject closed.")
            break

        elif choice in modules:
            name, filename = modules[choice]
            run_module(name, filename)

        elif choice == "13":
            pipeline = [
                "1", "2", "3", "4", "5", "6",
                "7", "8", "9", "10", "11", "12"
            ]

            for key in pipeline:
                name, filename = modules[key]

                if run_module(name, filename) != 0:
                    print("\nPipeline stopped due to an error.")
                    break
            else:
                print("\nComplete project pipeline finished!")

        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()
