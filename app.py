from flask import Flask, render_template, request, jsonify, session
import uuid

app = Flask(__name__)
app.secret_key = "scooter_secret_2024"

SCOOTERS = [
    {
        "id": 1,
        "name": "Volt X1",
        "tagline": "Urban Predator",
        "price": 1299,
        "range_km": 80,
        "top_speed": 45,
        "charge_time": 3.5,
        "motor_w": 500,
        "color": "#00f5d4",
        "emoji": "🛵",
        "tag": "Bestseller",
        "features": ["LED Display", "App Control", "USB Charging", "Anti-theft Lock"]
    },
    {
        "id": 2,
        "name": "Storm Pro",
        "tagline": "Built for Speed",
        "price": 1899,
        "range_km": 120,
        "top_speed": 60,
        "charge_time": 4,
        "motor_w": 1000,
        "color": "#f72585",
        "emoji": "⚡",
        "tag": "Performance",
        "features": ["Dual Motor", "Sport Mode", "GPS Tracker", "Hydraulic Brakes"]
    },
    {
        "id": 3,
        "name": "EcoRide S",
        "tagline": "Green & Lean",
        "price": 899,
        "range_km": 60,
        "top_speed": 35,
        "charge_time": 2.5,
        "motor_w": 350,
        "color": "#06d6a0",
        "emoji": "🌿",
        "tag": "Eco",
        "features": ["Foldable", "Lightweight", "Solar Assist", "Regenerative Braking"]
    },
    {
        "id": 4,
        "name": "Apex Ultra",
        "tagline": "Dominate Every Ride",
        "price": 2999,
        "range_km": 180,
        "top_speed": 80,
        "charge_time": 5,
        "motor_w": 2000,
        "color": "#ffd60a",
        "emoji": "🔥",
        "tag": "Premium",
        "features": ["Dual Battery", "AI Cruise Control", "Traction Control", "7-inch Display"]
    },
    {
        "id": 5,
        "name": "NightHawk",
        "tagline": "Own the Night",
        "price": 1599,
        "range_km": 100,
        "top_speed": 55,
        "charge_time": 3,
        "motor_w": 750,
        "color": "#7209b7",
        "emoji": "🌙",
        "tag": "Style",
        "features": ["LED Strip Lights", "Dark Mode App", "Stealth Mode", "NFC Unlock"]
    },
    {
        "id": 6,
        "name": "Titan Cargo",
        "tagline": "Work Hard, Ride Smart",
        "price": 2199,
        "range_km": 140,
        "top_speed": 50,
        "charge_time": 4.5,
        "motor_w": 1500,
        "color": "#fb8500",
        "emoji": "📦",
        "tag": "Cargo",
        "features": ["200kg Load", "Wide Deck", "Front Basket", "Fleet Management"]
    },
]

@app.route("/")
def index():
    return render_template("index.html", scooters=SCOOTERS)

@app.route("/api/cart", methods=["GET"])
def get_cart():
    return jsonify(session.get("cart", {}))

@app.route("/api/cart/add", methods=["POST"])
def add_to_cart():
    data = request.json
    sid = str(data.get("id"))
    cart = session.get("cart", {})
    cart[sid] = cart.get(sid, 0) + 1
    session["cart"] = cart
    return jsonify({"success": True, "cart": cart})

@app.route("/api/cart/remove", methods=["POST"])
def remove_from_cart():
    data = request.json
    sid = str(data.get("id"))
    cart = session.get("cart", {})
    if sid in cart:
        cart[sid] -= 1
        if cart[sid] <= 0:
            del cart[sid]
    session["cart"] = cart
    return jsonify({"success": True, "cart": cart})

@app.route("/api/checkout", methods=["POST"])
def checkout():
    cart = session.get("cart", {})
    if not cart:
        return jsonify({"success": False, "message": "Cart is empty!"})
    order_id = str(uuid.uuid4())[:8].upper()
    session["cart"] = {}
    return jsonify({"success": True, "order_id": order_id})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
