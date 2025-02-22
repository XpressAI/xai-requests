<p align="center">
  <a href="https://github.com/XpressAI/xircuits/tree/master/xai_components#xircuits-component-library-list">Component Libraries</a> •
  <a href="https://github.com/XpressAI/xircuits/tree/master/project-templates#xircuits-project-templates-list">Project Templates</a>
  <br>
  <a href="https://xircuits.io/">Docs</a> •
  <a href="https://xircuits.io/docs/Installation">Install</a> •
  <a href="https://xircuits.io/docs/category/tutorials">Tutorials</a> •
  <a href="https://xircuits.io/docs/category/developer-guide">Developer Guides</a> •
  <a href="https://github.com/XpressAI/xircuits/blob/master/CONTRIBUTING.md">Contribute</a> •
  <a href="https://www.xpress.ai/blog/">Blog</a> •
  <a href="https://discord.com/invite/vgEg2ZtxCw">Discord</a>
</p>

<p align="center"><i>Xircuits Component Library for HTTP Requests! Easily send GET requests and process responses.</i></p>

---
## Xircuits Component Library for HTTP Requests

This library enables Xircuits to perform HTTP GET requests seamlessly within workflows. It allows fetching data from web APIs and processing the responses efficiently.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Main Xircuits Components](#main-xircuits-components)
- [Installation](#installation)

## Prerequisites

Before you begin, you will need the following:

1. Python 3.9+.
2. Xircuits.

## Main Xircuits Components

### GetRequestComponent:
Performs a GET request to a specified URL and returns the response as a string.

<img src="https://github.com/user-attachments/assets/8cab4691-cbe2-425c-8284-efc2deacf321" alt="Image" width="250" height="100" />



## Installation

To use this component library, ensure that you have an existing [Xircuits setup](https://xircuits.io/docs/main/Installation). You can then install the HTTP Request library using the [component library interface](https://xircuits.io/docs/component-library/installation#installation-using-the-xircuits-library-interface), or through the CLI using:

```
xircuits install http-requests
```

You can also install it manually by cloning the repository:

```
# base Xircuits directory

git clone https://github.com/XpressAI/xai-http-requests xai_components/xai_http_requests
pip install -r xai_components/xai_http_requests/requirements.txt
```

