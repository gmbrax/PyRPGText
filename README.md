# pyRPGText
PyRPGText is a Python library for creating text-based adventures. With PyRPGText, you can focus on creating your game without worrying about the basic mechanics of an RPG. 

PyRPGText includes a story system based on blocks, a main character system with customizable attributes and levels, an event system for creating random or callable events, and an inventory system. 

These mechanics work out of the box but can be easily customized to fit your game's needs.
## Instalation
In the future the library will be available on PIP to be installed and used

## Usage
In this example we create a basic game with only 3 blocks, and run it
```python
# Here storySystem is imported to be used
from pyRPGText.system.story.storysystem import storySystem
#here storyBlock is imported to be used
from pyRPGText.system.story.storyblock import storyBlock


if __name__ == "__main__":
    st = storySystem() 
    sb1 = storyBlock("Block 1", """Once upon a time, there was a traveler who embarked on a journey to find a treasure."""
    """As he journeyed through the forest, he came across a path that split into two. One path led to the left, while """
    """the other path led to the right. The traveler had to make a decision and choose which path to take.""")
    sb2 = storyBlock("Block 2","""He chose to take the path to the left, which led him to a beautiful garden. """
    """As he explored the garden, he came across a fork in the road. He could either continue down the path to the right """
    """or take the path to the left.""")
    sb3 = storyBlock("Block 3","""The traveler decided to take the path to the right, which led him to a clearing where """
    """he encountered a fierce dragon. The dragon blocked the path, and the traveler knew he had to defeat it to """
    """continue on his journey.""")
    st.addStoryBlock(sb1)
    st.addStoryBlockBranch(sb1,sb2)
    st.addStoryBlockBranch(sb1,sb3)
    st.setInitialStoryBlock(sb1)
    st.run()
```

## Contributing
Help with this project is more than welcome.
Pull requests are welcome. For major changes please create and Issue to discuss the change to be made

## Author and acknowledgment
The author would like to thank to QuantumApprentice for the help, encouragement and testing the code.

## License
This project is under the LGPL-3.0 License