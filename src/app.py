from frontend import ExcelValidatorUI
from backend import process_excel

def main():
    ui = ExcelValidatorUI()
    ui.display()
    
    uploaded_file = ui.upload_file()
    if uploaded_file:
        result, errors = process_excel(uploaded_file)
        ui.display_result(result, errors)
        
    
if __name__ == "__main__":
    main()