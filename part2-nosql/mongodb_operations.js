use fleximart;

// Load product catalog data
db.products.insertMany(require('./products_catalog.json'));

// Find all Electronics products priced below 50000
db.products.find(
  { category: "Electronics", price: { $lt: 50000 } },
  { name: 1, price: 1, stock: 1, _id: 0 }
);

// Find products with average rating >= 4.0
db.products.aggregate([
  { $unwind: "$reviews" },
  { $group: { _id: "$name", avgRating: { $avg: "$reviews.rating" } } },
  { $match: { avgRating: { $gte: 4.0 } } }
]);

// Add a new review to product ELEC001
db.products.updateOne(
  { product_id: "ELEC001" },
  {
    $push: {
      reviews: {
        user: "U999",
        rating: 4,
        comment: "Good value",
        date: new Date()
      }
    }
  }
);

// Calculate average price by category
db.products.aggregate([
  {
    $group: {
      _id: "$category",
      avg_price: { $avg: "$price" },
      product_count: { $sum: 1 }
    }
  },
  { $sort: { avg_price: -1 } }
]);
