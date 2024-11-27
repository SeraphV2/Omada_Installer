

---

# Omada Controller Automation Script for Linux

This Python script automates the installation and update process of the TP-Link Omada Controller on Linux servers. Whether you're setting up a new server or keeping your existing Omada Controller up-to-date, this tool simplifies the process with minimal manual intervention.

## Features

- **Automated Installation**: Quickly set up the Omada Controller on any compatible Linux server.
- **Seamless Updates**: Update your existing Omada Controller to the latest version with ease.
- **Dependency Management**: Automatically detects and installs required dependencies.

## Requirements

- Python 3.6 or higher
- Root or sudo privileges on the server
- Internet access to fetch Omada Controller packages and dependencies

## Usage

1. Clone this repository:
   ```bash
   git clone https://github.com/SeraphV2/Omada_Installer.git
   cd Omada_Installer
   ```

2. Install required Python modules:
   ```bash
   sudo apt install python3-pip
   pip install -r requirements.txt
   ```

3. Run the script:
   ```bash
   chmod +x run.sh
   sh run.sh
   ```

4. Follow the prompts to install or update your Omada Controller.

## Roadmap

- Add support for other Linux distributions.
- Implement version rollback functionality.
- Improve configuration file support for advanced users.

## Contributions

Contributions, bug reports, and feature requests are welcome! Please open an issue or submit a pull request to help improve this tool.

## License

This project is licensed under the [MIT License](LICENSE).

---

