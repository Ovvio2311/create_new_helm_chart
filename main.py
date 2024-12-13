import os
import shutil

def create_helm_chart_template(sample_chart_path, new_chart_path, new_app_name):
    if not os.path.exists(sample_chart_path):
        print(f"Sample chart path '{sample_chart_path}' does not exist.")
        return

    # if os.path.exists(new_chart_path):
    #     print(f"New chart path '{new_chart_path}' already exists.")
    #     return

    # Create the new chart path
    # os.makedirs(new_chart_path)

    # Copy the sample chart to the new chart path
    shutil.copytree(sample_chart_path, new_chart_path, dirs_exist_ok=True)

    # Loop through the files in the new chart path and replace the app name
    for root, dirs, files in os.walk(new_chart_path):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, 'r') as f:
                content = f.read()
            content = content.replace('new-app-name', new_app_name)
            with open(file_path, 'w') as f:
                f.write(content)

    print(f"New Helm chart template created at '{new_chart_path}' with app name '{new_app_name}'.")

def check_and_create_helm_charts(apps_folder, sample_chart_path):
    for app_name in os.listdir(apps_folder):
        app_path = os.path.join(apps_folder, app_name)
        helm_chart_path = os.path.join(app_path, 'templates')

        if not os.path.exists(helm_chart_path):
            print(f"Helm chart not found for '{app_name}'. Creating new Helm chart template.")
            create_helm_chart_template(sample_chart_path, app_path, app_name)
        else:
            print(f"Helm chart already exists for '{app_name}'.")

# Example usage
apps_folder = "C:\\Users\\jacky\\source\\repos\\k8s_deployment\\k8s_yaml\\fyp"
sample_chart_path = "C:\\Users\\jacky\\source\\repos\\k8s_deployment\\helm_charts_example\\dotnet_web_api"

check_and_create_helm_charts(apps_folder, sample_chart_path)
