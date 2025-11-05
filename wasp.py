#!/usr/bin/env python3
"""
WASP - Wireless Asset Search Protocol
Advanced Mobile Intelligence Tool
Made by sid7.py
"""

import requests
import json
import sys
import argparse
import time

class WaspTool:
    def __init__(self):
        self.api_url = "https://dwxxyopsbstmftjbgmpt.supabase.co/functions/v1/fetch-mobile-details"
        self.session = requests.Session()
        self.session.headers.update({
            'Accept': 'application/json',
            'User-Agent': 'WASP/1.0'
        })

    def display_banner(self):
        banner = """
\x1b[38;5;81m
 ══════════════════════════════════════════════════════════════
                                                                            
  \x1b[38;5;201m██╗    ██╗ █████╗ ███████╗██████╗                      
  \x1b[38;5;201m██║    ██║██╔══██╗██╔════╝██╔══ ██╗                   
  \x1b[38;5;201m██║ █╗ ██║███████║███████╗██████╔╝    
  \x1b[38;5;201m██║███╗██║██╔══██║╚════██║██╔═══╝     
  \x1b[38;5;201m╚███╔███╔╝██║  ██║███████║██║         
  \x1b[38;5;201m ╚══╝╚══╝ ╚═╝  ╚═╝╚══════╝╚═╝         
                                                                
                Wireless Asset Search Protocol v2.1            
                     [MADE BY SID7.PY]                         
                                                                           
═══════════════════════════════════════════════════════════════
\x1b[0m
"""
        print(banner)

    def show_scan_animation(self, mobile):
        print(f"\n\x1b[38;5;226m[WASP] Initializing scan protocol for: {mobile}\x1b[0m")
        
        steps = [
            "Establishing secure connection...",
            "Bypassing carrier security...",
            "Querying cellular database...",
            "Analyzing network patterns...",
            "Compiling intelligence data..."
        ]
        
        for i, step in enumerate(steps, 1):
            print(f"\x1b[38;5;201m[{i}/5] {step}\x1b[0m")
            time.sleep(0.3)
        
        print("\x1b[38;5;46m[WASP] Scan complete! Retrieving results...\x1b[0m")

    def fetch_mobile_details(self, mobile):
        try:
            params = {'mobile': mobile}
            # Increased timeout to 40 seconds
            response = self.session.get(self.api_url, params=params, timeout=40)
            
            if response.status_code == 200:
                return response.json()
            else:
                return {"error": f"API Error: HTTP {response.status_code}"}
                
        except requests.exceptions.Timeout:
            return {"error": "Request timeout - Server took too long to respond (40s)"}
        except requests.exceptions.ConnectionError:
            return {"error": "Connection failed - Check your internet connection"}
        except requests.exceptions.RequestException as e:
            return {"error": f"Network error: {str(e)}"}
        except json.JSONDecodeError:
            return {"error": "Invalid response format from server"}

    def display_results(self, data, mobile):
        print(f"\n\x1b[38;5;81m╔════════════════════════════════════════════════════════════════╗")
        print(f"║                    SCAN RESULTS - {mobile}                    ║")
        print(f"╚════════════════════════════════════════════════════════════════╝\x1b[0m\n")
        
        if "error" in data:
            print(f"\x1b[38;5;196m❌ ERROR: {data['error']}\x1b[0m")
            print(f"\n\x1b[38;5;214m💡 TIPS:")
            print(f"• Check if the mobile number is valid")
            print(f"• Verify your internet connection")
            print(f"• The API server might be temporarily unavailable")
            print(f"• Try again after some time\x1b[0m")
            return

        if not data:
            print(f"\x1b[38;5;214m⚠️  No data found for mobile number: {mobile}\x1b[0m")
            return

        # Display data in organized format
        print("\x1b[38;5;201m" + "═" * 60 + "\x1b[0m")
        
        # Personal Information
        if 'name' in data:
            print(f"\x1b[38;5;201m🔹 NAME:\x1b[0m")
            print(f"   \x1b[38;5;46m{data['name']}\x1b[0m\n")
        
        if 'fname' in data:
            print(f"\x1b[38;5;201m🔹 FATHER'S NAME:\x1b[0m")
            print(f"   \x1b[38;5;46m{data['fname']}\x1b[0m\n")
        
        # Mobile Numbers
        print(f"\x1b[38;5;201m🔹 PRIMARY MOBILE:\x1b[0m")
        print(f"   \x1b[38;5;46m{data.get('mobile', 'N/A')}\x1b[0m\n")
        
        if 'alt' in data and data['alt']:
            print(f"\x1b[38;5;201m🔹 ALTERNATE MOBILE:\x1b[0m")
            print(f"   \x1b[38;5;46m{data['alt']}\x1b[0m\n")
        
        # Identification
        if 'id' in data:
            print(f"\x1b[38;5;201m🔹 ID:\x1b[0m")
            print(f"   \x1b[38;5;46m{data['id']}\x1b[0m\n")
        
        # Address Information
        if 'address' in data:
            print(f"\x1b[38;5;201m🔹 ADDRESS:\x1b[0m")
            address_lines = data['address'].split(', ')
            for line in address_lines:
                print(f"   \x1b[38;5;46m{line}\x1b[0m")
            print()
        
        # Service Provider
        if 'circle' in data:
            print(f"\x1b[38;5;201m🔹 SERVICE CIRCLE:\x1b[0m")
            print(f"   \x1b[38;5;46m{data['circle']}\x1b[0m\n")
        
        # Display any additional fields not covered above
        known_fields = {'name', 'mobile', 'alt', 'id', 'fname', 'address', 'circle'}
        additional_fields = set(data.keys()) - known_fields
        
        if additional_fields:
            print(f"\x1b[38;5;214m🔸 ADDITIONAL INFORMATION:\x1b[0m")
            for field in additional_fields:
                value = data[field]
                if value is not None:
                    field_display = field.replace('_', ' ').title()
                    print(f"   \x1b[38;5;201m{field_display}:\x1b[0m \x1b[38;5;46m{value}\x1b[0m")
            print()
        
        print("\x1b[38;5;201m" + "═" * 60 + "\x1b[0m")
        print(f"\x1b[38;5;46m✅ Scan completed successfully at {time.strftime('%H:%M:%S')}\x1b[0m")

    def validate_mobile(self, mobile):
        """Validate mobile number format"""
        mobile = mobile.strip()
        if not mobile.isdigit():
            return False, "Mobile number should contain only digits"
        if len(mobile) < 10:
            return False, "Mobile number too short"
        if len(mobile) > 15:
            return False, "Mobile number too long"
        return True, mobile

    def process_mobile(self, mobile):
        """Process a single mobile number"""
        is_valid, validation_result = self.validate_mobile(mobile)
        if not is_valid:
            print(f"\x1b[38;5;196m❌ Invalid mobile number: {validation_result}\x1b[0m")
            return False
        
        self.show_scan_animation(mobile)
        result = self.fetch_mobile_details(mobile)
        self.display_results(result, mobile)
        return True

    def run(self):
        parser = argparse.ArgumentParser(
            description='WASP - Advanced Mobile Intelligence Tool',
            formatter_class=argparse.RawDescriptionHelpFormatter,
            epilog="""
Examples:
  python wasp.py 9509972790          # Scan single number
  python wasp.py -f numbers.txt      # Scan multiple numbers from file
  python wasp.py                     # Interactive mode
            """
        )
        parser.add_argument('mobile', nargs='?', help='Mobile number to scan')
        parser.add_argument('-f', '--file', help='File containing mobile numbers (one per line)')
        
        args = parser.parse_args()
        
        self.display_banner()
        
        # File mode
        if args.file:
            try:
                with open(args.file, 'r') as f:
                    mobiles = [line.strip() for line in f if line.strip()]
                
                if not mobiles:
                    print(f"\x1b[38;5;196m❌ No valid mobile numbers found in file: {args.file}\x1b[0m")
                    return
                
                print(f"\x1b[38;5;214m📁 Processing {len(mobiles)} numbers from: {args.file}\x1b[0m")
                
                success_count = 0
                for i, mobile in enumerate(mobiles, 1):
                    print(f"\n\x1b[38;5;81m{'='*60}\x1b[0m")
                    print(f"\x1b[38;5;214m📱 Processing {i}/{len(mobiles)}: {mobile}\x1b[0m")
                    
                    if self.process_mobile(mobile):
                        success_count += 1
                    
                    # Small delay between requests to avoid overwhelming the API
                    if i < len(mobiles):
                        time.sleep(2)
                
                print(f"\n\x1b[38;5;46m✅ Successfully processed {success_count}/{len(mobiles)} numbers\x1b[0m")
                        
            except FileNotFoundError:
                print(f"\x1b[38;5;196m❌ File not found: {args.file}\x1b[0m")
                sys.exit(1)
            except Exception as e:
                print(f"\x1b[38;5;196m❌ Error reading file: {str(e)}\x1b[0m")
                sys.exit(1)
                
        # Single mobile mode
        elif args.mobile:
            self.process_mobile(args.mobile)
            
        # Interactive mode
        else:
            try:
                while True:
                    mobile = input("\n\x1b[38;5;226m[WASP] Enter mobile number (or 'quit' to exit): \x1b[0m").strip()
                    
                    if mobile.lower() in ['quit', 'exit', 'q']:
                        break
                    
                    if mobile:
                        self.process_mobile(mobile)
                    else:
                        print("\x1b[38;5;214m⚠️  Please enter a mobile number\x1b[0m")
                        
            except KeyboardInterrupt:
                print(f"\n\x1b[38;5;196m\n[WASP] Scan session terminated\x1b[0m")

def main():
    try:
        tool = WaspTool()
        tool.run()
    except KeyboardInterrupt:
        print(f"\n\x1b[38;5;196m❌ Scan terminated by user\x1b[0m")
        sys.exit(0)
    except Exception as e:
        print(f"\x1b[38;5;196m💥 Critical error: {str(e)}\x1b[0m")
        sys.exit(1)

if __name__ == "__main__":
    main()
