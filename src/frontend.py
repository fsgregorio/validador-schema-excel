import streamlit as st

class ExcelValidatorUI:

    def __init__(self):
        self.set_page_config()
        
        
    def set_page_config(self):
        st.set_page_config(
            page_title="Excel Validator",
            page_icon="📊",
            layout="centered",
            initial_sidebar_state="auto",
        )
        
    def display(self):
        st.title("Excel Validator")
        st.write("Upload an Excel file and we will validate it for you.")

    def upload_file(self):
        uploaded_file = st.file_uploader("Choose a file", type=["xlsx"])
        if uploaded_file is not None:
            return uploaded_file
        return None
    
    def display_result(self, result, errors):
        if errors:
            st.error("Errors founded🫠:")
            for error in errors:
                st.error(error)
        else:
            st.success("Files loaded sssssuccessfully!😉")
    
if __name__ == '__main__':
    app = ExcelValidatorUI()
    app.display()
