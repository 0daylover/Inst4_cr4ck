#!/usr/bin/env python3
"""
systemFunction
"""

import sys

try:
    from runner import *
    
    print("")
    
    monitor_loop()
    
except ImportError as e:
    print(f"❌ Error: {e}")
    print("💡 Make sure to compile first: python3 compile.py build_ext --inplace")
    sys.exit(1)
except KeyboardInterrupt:
    print("\n[INFO] stopped by user.")
    sys.exit(0)
except Exception as e:
    print(f"❌ Execution error: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
