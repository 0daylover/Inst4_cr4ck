#!/usr/bin/env python3
"""

"""

import sys

try:
    from setup import *
    
    print("")
    try:
        success = setup()
        if not success:
            print("\n[ERROR] Setup failed! Please check the error messages above.")
            sys.exit(1)
        else:
            print("\n[SUCCESS] Setup completed successfully!")
            sys.exit(0)
    except KeyboardInterrupt:
        print("\n[INFO] Setup interrupted by user.")
        sys.exit(1)
    except Exception as e:
        print(f"\n[ERROR] Unexpected error during setup: {e}")
        sys.exit(1)
        
except ImportError as e:
    print(f"❌ Error: {e}")
    print("💡 Make sure to compile first: python3 compile.py build_ext --inplace")
    sys.exit(1)
except Exception as e:
    print(f"❌ Execution error: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
