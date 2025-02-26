import flet as ft
from backend import HealthCheck

health_check = HealthCheck()

def main(page: ft.Page):
    page.title = "Bantay Kalusugan"

    name_input = ft.TextField(label="Name")
    age_input = ft.TextField(label="Age", keyboard_type=ft.KeyboardType.NUMBER)
    symptoms_input = ft.TextField(label="Symptoms")

    def submit_data(e):
        health_check.add_record(name_input.value, age_input.value, symptoms_input.value)
        update_records()

    def update_records():
        records = health_check.get_records()
        records_list.controls.clear()
        for record in records:
            records_list.controls.append(ft.Text(f"{record[1]}, {record[2]} years old - {record[3]}"))
        page.update()

    submit_button = ft.ElevatedButton("Submit", on_click=submit_data)
    records_list = ft.Column()

    page.add(name_input, age_input, symptoms_input, submit_button, records_list)
    update_records()

ft.app(target=main)

