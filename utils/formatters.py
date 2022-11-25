from datetime import datetime, timedelta


class format:
    def datetime(**kwargs) -> dict:
        date_string = kwargs.get("date", False)
        hour_string = kwargs.get("hour", False)
        data = {
            "fullDate": "",
            "date": "",
            "hour": "",
        }

        if bool(date_string) and bool(hour_string):
            date_values = [
                int(date_string[:4]),
                int(date_string[4:6]),
                int(date_string[6:]),
            ]
            hour_values = [
                int(hour_string[:2]),
                int(hour_string[2:4]),
                int(hour_string[4:]),
            ]

            full_data = datetime(*date_values, *hour_values) + timedelta(hours=-3)

            data["fullDate"] = full_data
            data["date"] = full_data.date()
            data["hour"] = full_data.time()

        return data

    def cpf(cpf: str) -> str:
        return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"

    def remove_space(string: str) -> str:
        return " ".join(string.split())