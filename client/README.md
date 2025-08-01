# Luxembourg Frontend

A web-based frontend interface for visualizing large language model (LLM) token generation and probability distributions in real-time. This project provides an interactive chat interface that displays uncertainty visualization and token-level analysis for LLM outputs.

## Overview

Luxembourg Frontend is a containerized web application that connects to an LLM visualization backend to provide:

- **Real-time Chat Interface**: Interactive chat with streaming LLM responses
- **Token Probability Visualization**: Bar charts showing probability distributions for each generated token
- **Uncertainty Display**: Visual indicators of model uncertainty through color-coded backgrounds
- **Token Editing**: Click on tokens in the probability chart to regenerate text from that point
- **SafeNudge™ Integration**: Optional safety features that can be toggled on/off
- **Configurable Parameters**: Adjustable random state, generation delay, and temperature settings

## Features

### Core Functionality
- **Streaming Response Display**: Real-time visualization of token generation
- **Interactive Token Selection**: Click on generated tokens to view their probability distributions
- **Alternative Path Exploration**: Select different tokens from probability charts to explore alternative generation paths
- **Uncertainty Visualization**: Background colors indicate model confidence levels
- **Parameter Control**: Fine-tune generation with random seed, delay, and other parameters

### Safety Features
- **SafeNudge™**: Optional safety layer that can restrict certain interactions
- **Probability Masking**: Hide probability information when safety features are enabled
- **Token Editing Protection**: Prevent token manipulation when safety mode is active

## Architecture

### Frontend Components
- **HTML Interface** (`main.html`): Responsive layout with chat interface and visualization panels
- **JavaScript Logic** (`js/main.js`): Handles API communication, streaming, and D3.js visualizations
- **CSS Styling** (`css/main.css`): Modern, dark-themed styling for the interface

### Backend Integration
- Connects to LLM visualization backend via HTTP API
- Supports two main endpoints:
  - `/generate`: Initial text generation with streaming response
  - `/regenerate`: Alternative generation from specific token positions

## Docker Configuration

This frontend is designed to run in a Docker container alongside the LLM backend service.

### Container Setup
- **Frontend Container**: Serves the web interface
- **Backend Container**: Named `llm-viz`, runs on port 8000
- **Network**: Both containers must be on the same Docker network

### API Configuration
The frontend is configured to communicate with the backend using:
```
Backend URL: http://llm-viz:8000
```

## File Structure

```
luxembourg-frontend/
├── Dockerfile              # Container build configuration
├── main.html               # Main web interface
├── README.md               # This documentation
├── css/
│   └── main.css            # Interface styling
├── js/
│   └── main.js             # Core application logic
└── kubernetes/
    ├── ingress.yml         # Kubernetes ingress configuration
    ├── kubernetes.yml      # Kubernetes deployment
    └── service.yml         # Kubernetes service definition
```

## Technology Stack

- **Frontend Framework**: jQuery for DOM manipulation and AJAX
- **Visualization**: D3.js v4 for interactive probability charts
- **Styling**: Custom CSS with modern dark theme
- **Container**: Docker for deployment
- **Orchestration**: Kubernetes support included

## Usage

### Basic Interaction
1. Enter a text prompt in the chat input field
2. Click the send button (►) to generate a response
3. Watch as tokens are generated in real-time with uncertainty visualization
4. Click on any generated token to view its probability distribution
5. Click on alternative tokens in the probability chart to explore different paths

### Advanced Controls
- **Random State**: Set a specific seed for reproducible generation
- **Delay Control**: Adjust generation speed (0-2 seconds between tokens)
- **Uncertainty Toggle**: Show/hide confidence visualization
- **SafeNudge™**: Enable safety restrictions

### Safety Features
When SafeNudge™ is enabled:
- Probability viewing is restricted
- Token editing is disabled
- Enhanced safety monitoring is active

## API Endpoints

### Generate Text
```
POST /generate
Parameters:
- init_prompt: Initial text prompt
- safenudge: Safety mode (true/false)
- k: Number of top tokens to consider (default: 20)
- T: Temperature for generation (default: 1.3)
- max_new_tokens: Maximum tokens to generate (default: 300)
- random_state: Random seed for reproducibility
- sleep_time: Delay between tokens (0-2 seconds)
```

### Regenerate from Token
```
POST /regenerate
Parameters:
- init_prompt: Original prompt
- content: Current generated content
- token_pos: Position to regenerate from
- new_token: Selected alternative token
- (same generation parameters as above)
```

## Development

### Local Development
1. Ensure the backend container `llm-viz` is running on port 8000
2. Serve the frontend files using a web server
3. Both services should be on the same network for communication

### Docker Deployment
1. Build the frontend container
2. Ensure backend container `llm-viz` is running
3. Deploy both containers on the same Docker network
4. Access the interface through the frontend container's exposed port

## Contributing

This project is part of large language model research infrastructure. When contributing:

1. Maintain compatibility with the existing API structure
2. Preserve the real-time streaming functionality
3. Test with both safety features enabled and disabled
4. Ensure responsive design across different screen sizes

## License

This project is part of academic research infrastructure for large language model visualization and analysis.