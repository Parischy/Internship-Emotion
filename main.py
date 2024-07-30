from deepface import DeepFace
import pandas as pd
import os


def analyze_images_in_folders(folder_paths):
    results = []
    errors = []

    for folder_path in folder_paths:
        for filename in os.listdir(folder_path):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                img_path = os.path.join(folder_path, filename)
                try:
                    analyses = DeepFace.analyze(
                        enforce_detection=False,
                        img_path=img_path,
                        actions=['age', 'gender', 'race', 'emotion'],
                    )
                    for i, analysis in enumerate(analyses):
                        analysis['file_path'] = img_path
                        analysis['face_number'] = i + 1  # Add face number starting from 1
                        results.append(analysis)
                except Exception as e:
                    errors.append(img_path)
                    print(f"Error analyzing {img_path}: {e}")

    return results, errors


def main():
    folder_paths = [
        "image/child",
        "image/teen",
        "image/adults"
    ]

    repeat = 5

    for index in range(repeat):
        results, errors = analyze_images_in_folders(folder_paths)

        df = pd.DataFrame(results)
        print("Analysis results DataFrame:")
        print(df)

        df.to_csv(f'result/deepface_analysis_results_{index}.csv', index=False)
        print(f"Analysis results saved to deepface_analysis_results_{index}.csv")

        if errors:
            print("\nImages that could not be analyzed:")
            for error in errors:
                print(error)
            with open(f'deepface_analysis_errors_{index}.txt', 'w') as f:
                for error in errors:
                    f.write(f"{error}\n")
            print(f"Error list saved to deepface_analysis_errors_{index}.txt")


if __name__ == "__main__":
    main()
