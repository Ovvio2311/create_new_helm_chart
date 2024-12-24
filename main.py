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
apps_folder = "C:\\Users\\jackyli\\source\\repos\\k8s_deployment\\k8s_yaml\\fyp"
sample_chart_path = "C:\\Users\\jackyli\\source\\repos\\k8s_deployment\\helm_charts_example\\k8s-app"

check_and_create_helm_charts(apps_folder, sample_chart_path)

# Create argocd template
def create_argocd_template(sample_argocd_path, new_argocd_path, new_app_name):
    if not os.path.exists(sample_argocd_path):
        print(f"Sample argocd path '{sample_argocd_path}' does not exist.")
        return

    shutil.copytree(sample_argocd_path, new_argocd_path, dirs_exist_ok=True)

    # Loop through the files in the new argocd and replace the app name
    for root, dirs, files in os.walk(new_argocd_path):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, 'r') as f:
                content = f.read()
            content = content.replace('new-app-name', new_app_name)
            with open(file_path, 'w') as f:
                f.write(content)

    print(f"New argocd template created at '{new_argocd_path}' with app name '{new_app_name}'.")

def check_and_create_argocd(apps_folder, sample_argocd_path):
    for app_name in os.listdir(apps_folder):
        app_path = os.path.join(apps_folder, app_name)
        argocd_path = os.path.join(app_path, '{app_name}.yaml')

        if not os.path.exists(argocd_path):
            print(f"argocd not found for '{app_name}'. Creating new argocd template.")
            create_argocd_template(sample_argocd_path, app_path, app_name)
        else:
            print(f"argocd already exists for '{app_name}'.")

# Example usage
apps_folder = "C:\\Users\\jackyli\\source\\repos\\k8s_deployment\\k8s_argocd_yaml\\fyp"
sample_argocd_path = "C:\\Users\\jackyli\\source\\repos\\k8s_deployment\\k8s_argocd_yaml\\new_argocd_template"

check_and_create_argocd(apps_folder, sample_argocd_path)