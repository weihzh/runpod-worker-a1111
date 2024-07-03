#!/bin/bash

echo "Cleaning data folder from csv files ..."
rm -f src/data/*.csv

echo "Choose environment:"
echo "1. Production"
echo "2. Stage"
echo "3. Test"
echo "4. Webui"
read -p "Enter your choice: " choice

case $choice in
    1)
        ./build_prod.sh
        ;;
    2)
        ./build_stage.sh
        ;;
    3)
        ./build_test.sh
        ;;
    4)
        ./build_webui.sh
        ;;
    *)
        echo "Invalid choice. Exiting."
        exit 1
        ;;
esac
