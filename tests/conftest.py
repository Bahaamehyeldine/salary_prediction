import os

# src/database.py builds a Supabase client at import time; give it harmless values.
os.environ.setdefault("SUPABASE_URL", "https://example.supabase.co")
os.environ.setdefault(
    "SUPABASE_KEY",
    "ci-placeholder-key",
)
