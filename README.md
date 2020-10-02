# GameStreamingAutomation

Flow is voice command to Google Assistant -> trigger script on Raspberry Pi -> wake PC using Wake On Lan (WOL) -> let PC wake up -> run the `moonlight stream` command

## Usage

You will need to have the following tools installed : 
* [python 3](https://www.python.org/downloads/) 
* [pip 3](https://pip.pypa.io/en/stable/)
* libcec-dev

Install the required dependencies:
```shell
pip3 install --user -r requirements.txt
```
You can add the MAC address of the PC you want to wake to an OS environment variable called `WOL_MAC` to remove the prompt each time
