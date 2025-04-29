import os, shutil, sys

src = sys.argv[1]
dst = sys.argv[2]
max_depth = int(sys.argv[3]) if sys.argv[3] else 0

for root, _, files in os.walk(src):
	for f in files:
		src_path = os.path.join(root, f)
		rel_path = os.path.relpath(root, src)
		
		parts = []
		if rel_path != ".":
			parts = rel_path.split(os.sep)
			if max_depth > 0:
				keep = max_depth - 1
				parts = parts[-keep:] if keep > 0 else []
		
		target_dir = os.path.join(dst, *parts) if parts else dst
		os.makedirs(target_dir, exist_ok=True)
		
		base, ext = os.path.splitext(f)
		dest = os.path.join(target_dir, f)
		count = 1
		
		while os.path.exists(dest):
			dest = os.path.join(target_dir, f"{base}_{count}{ext}")
			count += 1
		
		shutil.copy2(src_path, dest)