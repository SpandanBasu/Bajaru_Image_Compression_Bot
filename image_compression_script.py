import os
import time
from PIL import Image

# --- 1. CONFIGURATION & FOLDERS ---
# Input directories
RAW_THUMB_DIR = "raw/thumbnail_raw"
RAW_DETAIL_DIR = "raw/detail_raw"

# Output directories
OUT_THUMB_DIR = "output/thumbnails"
OUT_DETAIL_DIR = "output/details"

# Ensure all directories exist
for directory in [RAW_THUMB_DIR, RAW_DETAIL_DIR, OUT_THUMB_DIR, OUT_DETAIL_DIR]:
    os.makedirs(directory, exist_ok=True)

def process_thumbnails():
    print("\n--- 📏 Resizing Thumbnails (200x200) ---")
    # Supports common image formats
    files = [f for f in os.listdir(RAW_THUMB_DIR) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp'))]
    
    if not files:
        print(f"  No images found in {RAW_THUMB_DIR}.")
        return

    for filename in files:
        start_time = time.time()
        filepath = os.path.join(RAW_THUMB_DIR, filename)
        # Extract the product name from the filename
        product_name = os.path.splitext(filename)[0]
        
        try:
            with Image.open(filepath) as img:
                # 1. Resize to 200x200
                thumb_img = img.resize((200, 200), Image.Resampling.LANCZOS)
                
                # 2. Save with the new naming format: productname_small.webp
                # Lossless WebP is great for maintaining the clarity of your generated assets
                out_path = os.path.join(OUT_THUMB_DIR, f"{product_name}_small.webp")
                thumb_img.save(out_path, "WEBP", lossless=True)
            
            elapsed = time.time() - start_time
            print(f"  ✅ {filename} -> {product_name}_small.webp ({elapsed:.2f}s)")
            
        except Exception as e:
            print(f"  ❌ Failed to process {filename}: {e}")

def process_details():
    print("\n--- 🖼️ Resizing Detail Images (800x800) ---")
    files = [f for f in os.listdir(RAW_DETAIL_DIR) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp'))]
    
    if not files:
        print(f"  No images found in {RAW_DETAIL_DIR}.")
        return

    for filename in files:
        start_time = time.time()
        filepath = os.path.join(RAW_DETAIL_DIR, filename)
        product_name = os.path.splitext(filename)[0]
        
        try:
            with Image.open(filepath) as img:
                # Convert RGBA to RGB for standard detail photos (no transparency needed)
                if img.mode in ("RGBA", "P"):
                    img = img.convert("RGB")
                
                # 1. Resize to 800x800
                detail_img = img.resize((800, 800), Image.Resampling.LANCZOS)
                
                # 2. Save as optimized WebP
                out_path = os.path.join(OUT_DETAIL_DIR, f"{product_name}.webp")
                detail_img.save(out_path, "WEBP", quality=80)
            
            elapsed = time.time() - start_time
            print(f"  ✅ {filename} -> {product_name}_big.webp ({elapsed:.2f}s)")
            
        except Exception as e:
            print(f"  ❌ Failed to process {filename}: {e}")

if __name__ == "__main__":
    process_thumbnails()
    process_details()
    print("\n🎉 All Bajaru assets processed! Thumbnails follow the '_thumb' naming format.")