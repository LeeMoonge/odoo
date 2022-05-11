# -*- coding: utf-8 -*-
# @Time : 2022/5/11 14:42
# @Author : LeeMoonge

from odoo import models, fields


class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = '房地产广告模块'

    name = fields.Char(string='name')
    description = fields.Text(string='description')
    postcode = fields.Char(string='postcode')
    date_availability = fields.Date(string='date_availability')
    expected_price = fields.Float(string='expected_price')
    selling_price = fields.Float(string='selling_price')
    bedrooms = fields.Integer(string='bedrooms')
    living_area = fields.Integer(string='living_area')
    facades = fields.Integer(string='facades')
    garage = fields.Boolean(string='garage')
    garden = fields.Boolean(string='garden')
    garden_area = fields.Integer(string='garden_area')
    garden_orientation = fields.Selection([('North', '北'), ('South', '南'), ('East', '东'), ('West', '西')],
                                          string='garden_orientation')