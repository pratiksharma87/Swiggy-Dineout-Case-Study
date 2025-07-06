import os
from huggingface_hub import InferenceClient
from pydantic import BaseModel, condecimal

user_input = input("Enter a restaurant_id: ")

# Displaying the input
print("You entered restaurant_id:", user_input)

class RestaurantMetrics(BaseModel):
    restaurant_id: str
    restaurant_name: str
    locality: str
    cuisine: str
    date: str
    bookings: int
    cancellations: int
    customers: int
    avg_money_spend_per_customer: int
    net_revenue: int
    avg_rating: float


# Create an instance of the model (data conforming to the schema)
restaurant_dataset1 = {"restaurant_id": "R001", "restaurant_name": "Spice Garden", "locality": "Koramangala", "cuisine": "Indian","date": "2024-06-01", "bookings": 12, "cancellations": 2, "customers": 34, "avg_money_spend_per_customer": 500, "net_revenue": 17000, "avg_rating": 4.3}
restaurant_dataset2 = {"restaurant_id": "R002", "restaurant_name": "Little Italy", "locality": "Koramanagala", "cuisine": "Italian","date": "2024-06-01", "bookings": 14, "cancellations": 1, "customers": 38, "avg_money_spend_per_customer": 700, "net_revenue": 26600, "avg_rating": 4.4}
restaurant_dataset3 = {"restaurant_id": "R003", "restaurant_name": "Mainland China", "locality": "Koramangala", "cuisine": "Chinese","date": "2024-06-01", "bookings": 10, "cancellations": 2, "customers": 28, "avg_money_spend_per_customer": 650, "net_revenue": 18200, "avg_rating": 4.0}
restaurant_dataset4 = {"restaurant_id": "R004", "restaurant_name": "Udupi", "locality": "Koramangala", "cuisine": "Indian","date": "2024-06-01", "bookings": 300, "cancellations": 20, "customers": 1200, "avg_money_spend_per_customer": 500, "net_revenue": 600000, "avg_rating": 4.2}
restaurant_dataset5 = {"restaurant_id": "R005", "restaurant_name": "Pizza Hut", "locality": "Koramangala", "cuisine": "Italian","date": "2024-06-01", "bookings": 140, "cancellations": 15, "customers": 500, "avg_money_spend_per_customer": 600, "net_revenue": 300000, "avg_rating": 3.9}
restaurant_dataset6 = {"restaurant_id": "R006", "restaurant_name": "Wow Momos!", "locality": "Koramangala", "cuisine": "Chinese","date": "2024-06-01", "bookings": 200, "cancellations": 14, "customers": 600, "avg_money_spend_per_customer": 650, "net_revenue": 390000, "avg_rating": 4.0}

class AdsData(BaseModel):
    restaurant_id: str
    campaign_id: str
    campaign_start: str
    campaign_end: str
    impressions: int
    clicks: int
    conversions: int
    money_spend_on_ads: int
    revenue_generated_from_ads: int


ads_dataset1 = {"restaurant_id": "R001", "campaign_id": "C101", "campaign_start": "2024-05-01", "campaign_end": "2024-05-30", "impressions": 30000, "clicks": 2500, "conversions": 210, "money_spend_on_ads": 5000, "revenue_generated_from_ads": 18500}
ads_dataset2 = {"restaurant_id": "R002", "campaign_id": "C102", "campaign_start": "2024-05-01", "campaign_end": "2024-05-30", "impressions": 35000, "clicks": 3500, "conversions": 215, "money_spend_on_ads": 7000, "revenue_generated_from_ads": 21500}
ads_dataset3 = {"restaurant_id": "R003", "campaign_id": "C103", "campaign_start": "2024-05-01", "campaign_end": "2024-05-30", "impressions": 25000, "clicks": 2000, "conversions": 195, "money_spend_on_ads": 4500, "revenue_generated_from_ads": 16500}
ads_dataset4 = {"restaurant_id": "R004", "campaign_id": "C104", "campaign_start": "2024-05-01", "campaign_end": "2024-05-30", "impressions": 70000, "clicks": 9500, "conversions": 910, "money_spend_on_ads": 10000, "revenue_generated_from_ads": 290000}
ads_dataset5 = {"restaurant_id": "R005", "campaign_id": "C105", "campaign_start": "2024-05-01", "campaign_end": "2024-05-30", "impressions": 55000, "clicks": 6500, "conversions": 415, "money_spend_on_ads": 8000, "revenue_generated_from_ads": 100500}
ads_dataset6 = {"restaurant_id": "R006", "campaign_id": "C106", "campaign_start": "2024-05-01", "campaign_end": "2024-05-30", "impressions": 65000, "clicks": 7500, "conversions": 395, "money_spend_on_ads": 8500, "revenue_generated_from_ads": 126500}


class peerBenchmarks(BaseModel):
    locality: str
    cuisine: str
    avg_bookings: int
    avg_conversion_rate: condecimal(ge=0, le=100)
    avg_ads_spend: int
    avg_return_on_investment: str
    avg_net_revenue: int
    avg_rating: float


peerbenchmark_koramangala_Indian_cuisine = {"locality": "Koramangala", "cuisine": "Indian", "avg_bookings": 150, "avg_conversion_rate": 8, "avg_ads_spend": 5500, "avg_return_on_investment": "2.8x", "avg_net_revenue": 180000, "avg_rating": 4.1}
peerbenchmark_koramangala_Italian_cuisine = {"locality": "Koramangala", "cuisine": "Italian", "avg_bookings": 250, "avg_conversion_rate": 10, "avg_ads_spend": 7500, "avg_return_on_investment": "3.8x", "avg_net_revenue": 260000, "avg_rating": 4.2}
peerbenchmark_koramangala_Chinese_cuisine = {"locality": "Koramangala", "cuisine": "Chinese", "avg_bookings": 200, "avg_conversion_rate": 9, "avg_ads_spend": 6000, "avg_return_on_investment": "2.2x", "avg_net_revenue": 230000, "avg_rating": 4.0}


if (restaurant_dataset1.get("restaurant_id") == user_input and ads_dataset1.get("restaurant_id") == user_input):
    selected_restaurant_dataset = restaurant_dataset1
    selected_ads_dataset = ads_dataset1
    selected_peer_benchmark = peerbenchmark_koramangala_Indian_cuisine
elif (restaurant_dataset2.get("restaurant_id") == user_input and ads_dataset2.get("restaurant_id") == user_input):
    selected_restaurant_dataset = restaurant_dataset2
    selected_ads_dataset = ads_dataset2
    selected_peer_benchmark = peerbenchmark_koramangala_Italian_cuisine
elif (restaurant_dataset3.get("restaurant_id") == user_input and ads_dataset3.get("restaurant_id") == user_input):
    selected_restaurant_dataset = restaurant_dataset3
    selected_ads_dataset = ads_dataset3
    selected_peer_benchmark = peerbenchmark_koramangala_Chinese_cuisine
elif (restaurant_dataset4.get("restaurant_id") == user_input and ads_dataset4.get("restaurant_id") == user_input):
    selected_restaurant_dataset = restaurant_dataset4
    selected_ads_dataset = ads_dataset4
    selected_peer_benchmark = peerbenchmark_koramangala_Indian_cuisine
elif (restaurant_dataset5.get("restaurant_id") == user_input and ads_dataset5.get("restaurant_id") == user_input):
    selected_restaurant_dataset = restaurant_dataset5
    selected_ads_dataset = ads_dataset5
    selected_peer_benchmark = peerbenchmark_koramangala_Italian_cuisine
elif (restaurant_dataset6.get("restaurant_id") == user_input and ads_dataset6.get("restaurant_id") == user_input):
    selected_restaurant_dataset = restaurant_dataset6
    selected_ads_dataset = ads_dataset6
    selected_peer_benchmark = peerbenchmark_koramangala_Chinese_cuisine


client = InferenceClient(
    provider="novita",
    api_key=os.environ['HF_TOKEN'],
)

completion = client.chat.completions.create(
    model="meta-llama/Meta-Llama-3-8B-Instruct",
    messages=[
        {
            "role": "user",
            "content": "Generate a Textual Summary based on the data reports provided for the restaurant and its corresponding ads along with comparing to the peer benchmark data report provided for all restuarants in the same area"+ "Restaurant data report is:"+str(selected_restaurant_dataset)+ "Ads data report is:"+str(selected_ads_dataset)+ "Peer benchmark data report in same area is:"+str(selected_peer_benchmark)
        }
    ],
)

print(completion.choices[0].message)
