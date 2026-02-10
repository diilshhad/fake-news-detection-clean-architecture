import sys
import os

print(f"CWD: {os.getcwd()}")
print(f"Sys Path: {sys.path}")

try:
    import predict
    print("Successfully imported predict module")
    print(f"Model Path used: {predict.MODEL_PATH}")
except Exception as e:
    print(f"Failed to import predict: {e}")
    import traceback
    traceback.print_exc()
