<div align="center">
 <img src="https://upload.wikimedia.org/wikipedia/commons/8/81/TempleOS_logo.png" alt="TempleBot Logo" width="200" height="200">
 <h1>TempleBot</h1>
 <p>
   <b>A Discord bot dedicated to Terry Davis and TempleOS.</b>
 </p>
 <br>
</div>

TempleBot is a simple python Discord bot that provides useful information about [Terry Davis](https://en.wikipedia.org/wiki/Terry_A._Davis), the creator of [TempleOS](https://en.wikipedia.org/wiki/TempleOS), and his unique operating system, TempleOS. This bot aims to educate and inspire users about Terry Davis's remarkable journey, his accomplishments, and the fascinating world of TempleOS.

## Purpose

- Display biographical information about Terry Davis
- Explain the purpose and features of TempleOS
- Share interesting facts and quotes related to Terry Davis and TempleOS
- Provide links to relevant resources and documentation

## Setup

### Prerequisites

- Python 3.6 or higher
- `discord.py` library

### Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/TempleBot.git
```

2. Install the required dependencies:

```bash
cd TempleBot
pip install -r requirements.txt
```

3. Create a new Discord bot and obtain its token from the Discord Developer Portal.
  
4. Set the bot token as an environment variable named ``DISCORD_BOT_TOKEN``.

5. Run the bot:

```bash
python main.py
```

## Usage

Once the bot is running, you can interact with it using the following commands:

- `!terry`: Get biographical information about Terry Davis.
- `!templeos`: Learn about the TempleOS operating system.
- `!fact`: Receive an interesting fact or quote about Terry Davis or TempleOS.
- `!gif`: Recieve a random Terry David or TempleOS related GIF, some GIFs are more rare to occur than others.
- `!resources`: Get links to relevant resources and documentation.

## Contributing

> [!NOTE]
> Contributions are welcome! If you find any issues or want to add new features, feel free to open an issue or submit a pull request.

Here's how you can contribute:

1. Fork the repository
   
2. Create a new branch:

```bash
git checkout -b my-new-feature
```
3. Make your changes and then add them:

 ```bash
git add --all
```

4. Make your changes and commit them:

```bash
git commit -am 'Add some feature'
```

5. Push to the branch:

```bash
git push origin my-new-feature
```

5. Submit a pull request
   
## JSON File Structure
The bot uses JSON files to store quotes and GIFs. Here's an explanation of the structure:

### Quotes

The ``quotes.json`` file contains an array of ``quotes``. Each quote is a ``string``. Here's an example:

```json
{
    "quotes": [
        "This is a quote!"
    ]
}
```
> [!IMPORTANT]
> To add a new quote, simply append it to the ``quotes`` array.

### GIFs
   
The ``gifs.json`` file contains an array of GIF objects. Each object has two properties: ``url`` (the URL of the GIF) and ``probability`` (an integer representing the probability of displaying the GIF). Here's an example:

```json
{
    "gifs": [
      {
        "url": "https://example.com/gif1.gif",
        "probability": 90
      },
      {
        "url": "https://example.com/gif2.gif",
        "probability": 90
      },
      {
        "url": "https://example.com/gif3.gif",
        "probability": 15
      }
    ]
}
```
> [!IMPORTANT]
> To add a new GIF, append a new object to the ``gifs`` array with the appropriate ``url`` and ``probability`` values.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- [Terry Davis](https://en.wikipedia.org/wiki/Terry_A._Davis) for his remarkable work on TempleOS.
- The Discord.py library and its contributors for providing a powerful Python API for building Discord bots.

## Show Your Support

If you find this project valuable, please consider giving it a ⭐️ on GitHub!
