from db.entities.brand import Brand  # Product is its children
from db.entities.category import Category  # Product is its children
from db.entities.product import Product  # Brand and Category is its parents | Item is its son

from db.entities.consumer import Consumer  # Transaction is its children
from db.entities.store import Store  # Transaction is its children
from db.entities.item import Item  # Father of commercialized_item
from db.entities.transaction import Transaction  # Son of consumer and store | Father of commercialized_item
from db.entities.commercialized_item import CommercializedItem  # Transaction and item is its parents
