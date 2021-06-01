# -*- coding: utf-8 -*-

from odoo.tools import image
from odoo import models, fields, api


class hotel_managment_system(models.Model):
    _name = 'hotel_managment_system_hotel_managment_system'
    _description = 'hotel_managment_system_hotel_managment_system'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100

    


class Doctor(models.Model):
    _name = 'hotel_managment_system_doctor'
    _description = 'hotel_managment_system_doctor'

    first_name = fields.Char()
    last_name = fields.Char()
    img = fields.Image()
    patients  = fields.Many2many('hotel_managment_system_patient','hotel_managment_system_patient_doctor')
    departments  = fields.Many2many('hotel_managment_system_department','hotel_managment_system_department_doctor')


class Department(models.Model):
    _name = 'hotel_managment_system_department'
    _description = 'hotel_managment_system_department'

    name = fields.Char()
    capacity = fields.Integer()
    is_opened = fields.Boolean()
    patients= fields.Many2many('hotel_managment_system_patient','hotel_managment_system_patient_department')
    doctors  = fields.Many2many('hotel_managment_system_doctor','hotel_managment_system_department_doctor')
    # _sql_constraints = [
    #     ('hotel_managment_system_doctor_id', 'check(1==1)', 'Name must be unique.')
    # ]


class Patient(models.Model):
    _name = 'hotel_managment_system_patient'
    _description = 'hotel_managment_system_patient'

    first_name = fields.Char()
    last_name = fields.Char()
    bityh_date = fields.Date()
    history = fields.Html()
    cr_ratio= fields.Float()
    bllod_type= fields.Selection(
        [('A', 'A'), ('O', 'O')], default='A')
    pcr = fields.Boolean()
    image = fields.Binary()
    address = fields.Text()
    age = fields.Integer()
    departments = fields.Many2many('hotel_managment_system_department','hotel_managment_system_patient_department')
    doctors  = fields.Many2many('hotel_managment_system_doctor','hotel_managment_system_patient_doctor')

    @api.onchange('age')
    def on_change(self):
        if self.age < 30:
            self.pcr = True
        else:
            self.pcr = False
