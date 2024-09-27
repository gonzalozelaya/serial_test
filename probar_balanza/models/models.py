# -*- coding: utf-8 -*-

from odoo import models, fields, api
import serial
from odoo.exceptions import UserError
class SerialTest(models.Model):
    
    def show_serial(self):
        s = serial.Serial('COM7')
        res = s.read()
        raise UserError(res)
# class my_module(models.Model):
#     _name = 'my_module.my_module'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100