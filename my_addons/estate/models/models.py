# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class estate(models.Model):
#     _name = 'estate.estate'
#     _description = 'estate.estate'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

from odoo import models, fields


class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = '房地产广告模块'

    name = fields.Char(string='Title', default="Unknown")
    description = fields.Text(string='description')
    postcode = fields.Char(string='Postcode')
    date_availability = fields.Date(string='Availability From')
    expected_price = fields.Float(string='Expected Price')
    selling_price = fields.Float(string='Selling Price')
    bedrooms = fields.Integer(string='Bedrooms')
    living_area = fields.Integer(string='Living Area')
    facades = fields.Integer(string='facades')
    garage = fields.Boolean(string='garage')
    garden = fields.Boolean(string='garden')
    garden_area = fields.Integer(string='garden_area')
    garden_orientation = fields.Selection([('North', '北'), ('South', '南'), ('East', '东'), ('West', '西')],
                                          string='garden_orientation')
    last_seen = fields.Datetime("Last Seen", default=lambda self: fields.Datetime.now())
