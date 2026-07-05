from pydantic import BaseModel, Field
from typing import Optional
import json

class Review(BaseModel):
    key_themes: list[str] = Field(description="List all the key themes discussed in the review")
    summary: str = Field(description="A short summary of the review")
    sentiment: str = Field(description="Overall sentiment: positive, negative, or neutral")
    pros: Optional[list[str]] = Field(default=None, description="List of pros")
    cons: Optional[list[str]] = Field(default=None, description="List of cons")
    reviewer_name: Optional[str] = Field(default=None, description="Name of the reviewer if mentioned")


# Generate Schema
schema = Review.model_json_schema()

# Save to file
with open("review_schema.json", "w", encoding="utf-8") as f:
    json.dump(schema, f, indent=2, ensure_ascii=False)

print("✅ Schema successfully saved as 'review_schema.json'")