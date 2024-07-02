#!/bin/bash

# Define the header files to be included
HEADERS=(
    "#include <string.h>"
    "#include <stdlib.h>"
)

# Function to add headers to a file
add_headers() {
    local file="$1"
    local tmpfile=$(mktemp)

    # Write headers to the temporary file
    for header in "${HEADERS[@]}"; do
        echo "$header" >> "$tmpfile"
    done

    # Add a newline for separation
    echo "" >> "$tmpfile"

    # Append the original file content to the temporary file
    cat "$file" >> "$tmpfile"

    # Replace the original file with the temporary file
    mv "$tmpfile" "$file"
}

# Iterate over all .c files in the current directory
for cfile in *.c; do
    if [[ -f "$cfile" ]]; then
        echo "Adding headers to $cfile"
        add_headers "$cfile"
    fi
done

echo "Headers added to all C files."
