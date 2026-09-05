#!/bin/bash
# Double-click this file to see the MMT39 briefing.
cd "$(dirname "$0")"
clear
python3 model/mmt39.py --briefing
echo
echo "════════════════════════════════════════════════════════════════"
echo " Other things you can run (copy a line into Terminal):"
echo
echo "   python3 model/mmt39.py --lines        line economics"
echo "   python3 model/mmt39.py --media        advertising costs"
echo "   python3 model/mmt39.py --demo         a full worked year"
echo "   python3 model/mmt39.py --promotions 6 promotion costs at EUR 6"
echo "════════════════════════════════════════════════════════════════"
echo
echo "Press any key to close."
read -n 1
