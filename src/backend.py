import pandas as pd
from pydantic import ValidationError
from contract import Sales
from dotenv import load_dotenv
import os

def process_excel(uploaded_file):
    try:
        df = pd.read_excel(uploaded_file)
        errors = []
        
        # Verify if there are extra columns in the Dataframe
        extra_columns = set(df.columns) - set(Sales.model_fields.keys())
        if extra_columns:
            errors.append(f"Extra columns found: {', '.join(extra_columns)}")
            
        # Verify if there are missing columns in the Dataframe
        missing_columns = set(Sales.model_fields.keys()) - set(df.columns)
        if missing_columns:
            errors.append(f"Missing columns found: {', '.join(missing_columns)}")
            
        for index, row in df.iterrows():
            try:
                Sales(**row.to_dict())
            except ValidationError as ve:
                for err in ve.errors():
                    # 'loc' indica qual campo (ou campos) apresentou erro
                    field_path = " -> ".join(str(loc) for loc in err.get("loc", []))
                    error_message = err.get("msg", "Unknown error")
                    errors.append(f"Row {index + 2} - Field '{field_path}': {error_message}")
            except Exception as e:

                errors.append(f"Row {index + 2}: {str(e)}")
                
                # If there are any errors, return them
        return True, errors
    
    except Exception as e:
        return None, [str(e)]