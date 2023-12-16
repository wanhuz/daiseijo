class Util:
    def clean_drag_and_drop_quote(fname : str) -> str:
        if ("'" in fname[0]):
            new_name = fname.replace("'", "")
        elif ('"' in fname[0]):
            new_name = fname.replace('"', '')
        else:
            new_name = fname

        return new_name