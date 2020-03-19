from odoo import models, api, fields
class Book(models.Model):
    _name="library.book"
    book_id=fields.Integer(string="Book ID",required=True)
    customer_id=fields.Many2one('library.customer',string="Customer_id")
    author=fields.Text(string="Author",required=True)
    editor=fields.Char(string="Editor",required=True)
    edition=fields.Char(string="Year of Edition",required=True)
    isbn=fields.Char(string="ISBN",required=True)
    issue_date=fields.Date()
    return_date=fields.Date()


class Customer(models.Model):
    _name="library.customer"
    book_id=fields.One2many('library.book','book_id',string="Book id")
    customer_id=fields.Integer(string="Customer_id",required=True)
    name=fields.Char(string="Name",required=True)
    address=fields.Char(string="Address",required=True)
    email=fields.Char(string="Email",required=True)
