import json
import os

ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), '..'))

# block_category = input("Input category name: ")
arch_ex_block = input("Input Arch-Ex block name: ")
minecraft_block = input("Input Minecraft block name: ")
namespace = input("Input mod namespace or skip if you're using the \"minecraft:\" namespace: ")
recipe_item = input("Input recipe item name: ")

if len(namespace) == 0:
    namespace = "minecraft"

blockstate_dict = {
    "variants": {
        "facing=east,half=bottom,shape=inner_left": {
            "model": f"architecture_extensions:block/moldings/{arch_ex_block}_crown_molding_inner",
            "y": 270,
            "uvlock": True
        },
        "facing=east,half=bottom,shape=inner_right": {
            "model": f"architecture_extensions:block/moldings/{arch_ex_block}_crown_molding_inner"
        },
        "facing=east,half=bottom,shape=outer_left": {
            "model": f"architecture_extensions:block/moldings/{arch_ex_block}_crown_molding_outer",
            "y": 270,
            "uvlock": True
        },
        "facing=east,half=bottom,shape=outer_right": {
            "model": f"architecture_extensions:block/moldings/{arch_ex_block}_crown_molding_outer"
        },
        "facing=east,half=bottom,shape=straight": {
            "model": f"architecture_extensions:block/moldings/{arch_ex_block}_crown_molding"
        },
        "facing=east,half=top,shape=inner_left": {
            "model": f"architecture_extensions:block/moldings/{arch_ex_block}_crown_molding_inner",
            "x": 180,
            "uvlock": True
        },
        "facing=east,half=top,shape=inner_right": {
            "model": f"architecture_extensions:block/moldings/{arch_ex_block}_crown_molding_inner",
            "x": 180,
            "y": 90,
            "uvlock": True
        },
        "facing=east,half=top,shape=outer_left": {
            "model": f"architecture_extensions:block/moldings/{arch_ex_block}_crown_molding_outer",
            "x": 180,
            "uvlock": True
        },
        "facing=east,half=top,shape=outer_right": {
            "model": f"architecture_extensions:block/moldings/{arch_ex_block}_crown_molding_outer",
            "x": 180,
            "y": 90,
            "uvlock": True
        },
        "facing=east,half=top,shape=straight": {
            "model": f"architecture_extensions:block/moldings/{arch_ex_block}_crown_molding",
            "x": 180,
            "uvlock": True
        },
        "facing=north,half=bottom,shape=inner_left": {
            "model": f"architecture_extensions:block/moldings/{arch_ex_block}_crown_molding_inner",
            "y": 180,
            "uvlock": True
        },
        "facing=north,half=bottom,shape=inner_right": {
            "model": f"architecture_extensions:block/moldings/{arch_ex_block}_crown_molding_inner",
            "y": 270,
            "uvlock": True
        },
        "facing=north,half=bottom,shape=outer_left": {
            "model": f"architecture_extensions:block/moldings/{arch_ex_block}_crown_molding_outer",
            "y": 180,
            "uvlock": True
        },
        "facing=north,half=bottom,shape=outer_right": {
            "model": f"architecture_extensions:block/moldings/{arch_ex_block}_crown_molding_outer",
            "y": 270,
            "uvlock": True
        },
        "facing=north,half=bottom,shape=straight": {
            "model": f"architecture_extensions:block/moldings/{arch_ex_block}_crown_molding",
            "y": 270,
            "uvlock": True
        },
        "facing=north,half=top,shape=inner_left": {
            "model": f"architecture_extensions:block/moldings/{arch_ex_block}_crown_molding_inner",
            "x": 180,
            "y": 270,
            "uvlock": True
        },
        "facing=north,half=top,shape=inner_right": {
            "model": f"architecture_extensions:block/moldings/{arch_ex_block}_crown_molding_inner",
            "x": 180,
            "uvlock": True
        },
        "facing=north,half=top,shape=outer_left": {
            "model": f"architecture_extensions:block/moldings/{arch_ex_block}_crown_molding_outer",
            "x": 180,
            "y": 270,
            "uvlock": True
        },
        "facing=north,half=top,shape=outer_right": {
            "model": f"architecture_extensions:block/moldings/{arch_ex_block}_crown_molding_outer",
            "x": 180,
            "uvlock": True
        },
        "facing=north,half=top,shape=straight": {
            "model": f"architecture_extensions:block/moldings/{arch_ex_block}_crown_molding",
            "x": 180,
            "y": 270,
            "uvlock": True
        },
        "facing=south,half=bottom,shape=inner_left": {
            "model": f"architecture_extensions:block/moldings/{arch_ex_block}_crown_molding_inner"
        },
        "facing=south,half=bottom,shape=inner_right": {
            "model": f"architecture_extensions:block/moldings/{arch_ex_block}_crown_molding_inner",
            "y": 90,
            "uvlock": True
        },
        "facing=south,half=bottom,shape=outer_left": {
            "model": f"architecture_extensions:block/moldings/{arch_ex_block}_crown_molding_outer"
        },
        "facing=south,half=bottom,shape=outer_right": {
            "model": f"architecture_extensions:block/moldings/{arch_ex_block}_crown_molding_outer",
            "y": 90,
            "uvlock": True
        },
        "facing=south,half=bottom,shape=straight": {
            "model": f"architecture_extensions:block/moldings/{arch_ex_block}_crown_molding",
            "y": 90,
            "uvlock": True
        },
        "facing=south,half=top,shape=inner_left": {
            "model": f"architecture_extensions:block/moldings/{arch_ex_block}_crown_molding_inner",
            "x": 180,
            "y": 90,
            "uvlock": True
        },
        "facing=south,half=top,shape=inner_right": {
            "model": f"architecture_extensions:block/moldings/{arch_ex_block}_crown_molding_inner",
            "x": 180,
            "y": 180,
            "uvlock": True
        },
        "facing=south,half=top,shape=outer_left": {
            "model": f"architecture_extensions:block/moldings/{arch_ex_block}_crown_molding_outer",
            "x": 180,
            "y": 90,
            "uvlock": True
        },
        "facing=south,half=top,shape=outer_right": {
            "model": f"architecture_extensions:block/moldings/{arch_ex_block}_crown_molding_outer",
            "x": 180,
            "y": 180,
            "uvlock": True
        },
        "facing=south,half=top,shape=straight": {
            "model": f"architecture_extensions:block/moldings/{arch_ex_block}_crown_molding",
            "x": 180,
            "y": 90,
            "uvlock": True
        },
        "facing=west,half=bottom,shape=inner_left": {
            "model": f"architecture_extensions:block/moldings/{arch_ex_block}_crown_molding_inner",
            "y": 90,
            "uvlock": True
        },
        "facing=west,half=bottom,shape=inner_right": {
            "model": f"architecture_extensions:block/moldings/{arch_ex_block}_crown_molding_inner",
            "y": 180,
            "uvlock": True
        },
        "facing=west,half=bottom,shape=outer_left": {
            "model": f"architecture_extensions:block/moldings/{arch_ex_block}_crown_molding_outer",
            "y": 90,
            "uvlock": True
        },
        "facing=west,half=bottom,shape=outer_right": {
            "model": f"architecture_extensions:block/moldings/{arch_ex_block}_crown_molding_outer",
            "y": 180,
            "uvlock": True
        },
        "facing=west,half=bottom,shape=straight": {
            "model": f"architecture_extensions:block/moldings/{arch_ex_block}_crown_molding",
            "y": 180,
            "uvlock": True
        },
        "facing=west,half=top,shape=inner_left": {
            "model": f"architecture_extensions:block/moldings/{arch_ex_block}_crown_molding_inner",
            "x": 180,
            "y": 180,
            "uvlock": True
        },
        "facing=west,half=top,shape=inner_right": {
            "model": f"architecture_extensions:block/moldings/{arch_ex_block}_crown_molding_inner",
            "x": 180,
            "y": 270,
            "uvlock": True
        },
        "facing=west,half=top,shape=outer_left": {
            "model": f"architecture_extensions:block/moldings/{arch_ex_block}_crown_molding_outer",
            "x": 180,
            "y": 180,
            "uvlock": True
        },
        "facing=west,half=top,shape=outer_right": {
            "model": f"architecture_extensions:block/moldings/{arch_ex_block}_crown_molding_outer",
            "x": 180,
            "y": 270,
            "uvlock": True
        },
        "facing=west,half=top,shape=straight": {
            "model": f"architecture_extensions:block/moldings/{arch_ex_block}_crown_molding",
            "x": 180,
            "y": 180,
            "uvlock": True
        }
    }
}

crown_molding_straight = {
    "parent": "architecture_extensions:block/templates/template_crown_molding",
    "textures": {
        "texture": f"{namespace}:block/{minecraft_block}"
    }
}

crown_molding_inner = {
    "parent": "architecture_extensions:block/templates/template_crown_molding_inner",
    "textures": {
        "texture": f"{namespace}:block/{minecraft_block}"
    }
}

crown_molding_outer = {
    "parent": "architecture_extensions:block/templates/template_crown_molding_outer",
    "textures": {
        "texture": f"{namespace}:block/{minecraft_block}"
    }
}

item_model = {
    "parent": f"architecture_extensions:block/moldings/{arch_ex_block}_crown_molding"
}

recipe_dict = {
    "type": "minecraft:stonecutting",
    "ingredient": {
        "item": f"{namespace}:{recipe_item}"
    },
    "result": f"architecture_extensions:{arch_ex_block}_crown_molding",
    "count": 6
}

files = [blockstate_dict, crown_molding_straight, item_model, recipe_dict]
directories = [
    "assets\\architecture_extensions\\blockstates",
    "assets\\architecture_extensions\\models\\block\\moldings",
    "assets\\architecture_extensions\\models\\item",
    "data\\architecture_extensions\\recipes"
]

for i, j in zip(files, directories):
    os.chdir(f"{ROOT_DIR}\\src\\main\\resources\\{j}")
    with open(f"{arch_ex_block}_crown_molding.json", "w") as file:
        json.dump(i, file, indent=4)
        file.close()

os.chdir(f"{ROOT_DIR}\\src\\main\\resources\\assets\\architecture_extensions\\models\\block\\moldings")
with open(f"{arch_ex_block}_crown_molding_inner.json", "w") as file:
    json.dump(crown_molding_inner, file, indent=4)
    file.close()
with open(f"{arch_ex_block}_crown_molding_outer.json", "w") as file:
    json.dump(crown_molding_outer, file, indent=4)
    file.close()
print(f"Files for {arch_ex_block.title()} crown_molding have been generated")
