import os
import hashlib
import json

# Load known file signatures (magic bytes)
SIGNATURES = {
    "jpg": ["FFD8FF"],
    "png": ["89504E47"],
    "gif": ["47494638"],
    "pdf": ["25504446"],
    "zip": ["504B0304"],
    "exe": ["4D5A"],
    "rar": ["52617221"]
}

def get_file_hash(file_path, algo="sha256"):
    """Generate file hash for malware hinting."""
    hash_func = hashlib.new(algo)
    with open(file_path, "rb") as f:
        while chunk := f.read(4096):
            hash_func.update(chunk)
    return hash_func.hexdigest()

def identify_file_type(file_path):
    """Detect real file type using magic bytes."""
    with open(file_path, "rb") as f:
        file_header = f.read(8).hex().upper()

    for filetype, signatures in SIGNATURES.items():
        for sig in signatures:
            if file_header.startswith(sig):
                return filetype
    return "unknown"

def scan_file(file_path):
    """Compare detected file type vs. extension."""
    real_type = identify_file_type(file_path)
    ext = os.path.splitext(file_path)[1][1:].lower()
    file_hash = get_file_hash(file_path)

    status = "SAFE ✅" if real_type == ext else "⚠️ SUSPICIOUS!"
    return {
        "file_name": os.path.basename(file_path),
        "extension": ext or "none",
        "real_type": real_type,
        "status": status,
        "sha256": file_hash
    }

if __name__ == "__main__":
    path = input("Enter file path to scan: ").strip()
    if os.path.exists(path):
        result = scan_file(path)
        for k, v in result.items():
            print(f"{k.title():<12}: {v}")
    else:
        print("❌ File not found!")
