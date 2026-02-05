#!/bin/bash

echo "🚀 Starting LLM Council..."
echo ""

# Navigate to project directory
cd "$(dirname "$0")"

# Install Python dependencies if needed
echo "📦 Checking Python dependencies..."
if ! /usr/bin/pip3 show streamlit &> /dev/null; then
    echo "Installing dependencies..."
    /usr/bin/pip3 install --break-system-packages -r requirements.txt
    echo "✅ Dependencies installed successfully!"
else
    echo "✅ Dependencies already installed"
fi

# Set up PATH for streamlit
export PATH="$HOME/.local/bin:$PATH"

# Start Streamlit app
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  🧠 LLM Council"
echo "  Multi-agent AI reasoning system"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "Starting Streamlit server..."
echo "The app will open in your browser"
echo ""

# Run streamlit
streamlit run app.py
