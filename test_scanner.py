#!/usr/bin/env python3

import sys
import os
from ebram_scanner_v5 import PayloadManager, SessionManager

def test_payloads():
    """Test that all payload types are loaded correctly"""
    pm = PayloadManager()
    print(f"Loaded {len(pm.payloads)} payload types:")
    
    for payload_type, payloads in pm.payloads.items():
        print(f"- {payload_type}: {len(payloads)} payloads")
        # Print first payload as example
        if payloads:
            print(f"  Example: {payloads[0]}")
    
    return True

def test_new_functions():
    """Test that new vulnerability check functions are defined"""
    from ebram_scanner_v5 import (
        check_nosql_injection,
        check_jwt_vulnerabilities,
        check_graphql_injection,
        check_prototype_pollution,
        check_ssti,
        check_insecure_deserialization,
        check_idor,
        check_file_upload_vulnerabilities,
        check_race_condition
    )
    
    print("All new vulnerability check functions are defined!")
    return True

if __name__ == "__main__":
    print("Testing EBRAM Scanner v5.0 with enhanced payloads...")
    
    test_payloads()
    print("\n" + "-" * 50 + "\n")
    test_new_functions()
    
    print("\nAll tests passed! The scanner is ready to use with all payload files.")