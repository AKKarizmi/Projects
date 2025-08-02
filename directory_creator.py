import os

dirs_list = [
    'Health + Non-Criminal', 'English Prof', 'CV - GSH', 'L.O.R', 'IDs',
    'Work Experience', 'Videos', 'Monograph', 'Photos', 'Supporting DOCS',
    'School DOCS', 'University DOCS', 'Study Plan - GSH', 'Bank Statement',
    'Acceptance', 'Application Form', 'Submission Form'
]

path = r"G:\My Drive\Master's DB\076. Abidullah Ahmadzai"

existing_dirs = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
print(f'{existing_dirs} found in {path}')

for dir_name in dirs_list:
    full_path = os.path.join(path, dir_name)
    if not os.path.exists(full_path):
        os.mkdir(full_path)
        print(f"Created: {full_path}")
    else:
        print(f"Already exists: {full_path}")
