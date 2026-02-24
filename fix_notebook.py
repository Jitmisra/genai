import json

with open('/Users/agnik/Desktop/genai/GENAI_Midsem_Submission (1).ipynb', 'r') as f:
    nb = json.load(f)

# The last cell has the error
last_cell = nb['cells'][-2] # The last one is an empty cell, the second to last has the code
if last_cell['cell_type'] == 'code' and "px.figure(" in last_cell['source'][0]:
    last_cell['source'] = [
        "import matplotlib.pyplot as plt\n",
        "\n",
        "location_demand = demand_df.groupby('Charging Station Location')['Total_Demand'].sum().reset_index()\n",
        "\n",
        "plt.figure(figsize=(12, 6))\n",
        "plt.bar(location_demand['Charging Station Location'],\n",
        "        location_demand['Total_Demand'],\n",
        "        color='skyblue',\n",
        "        edgecolor='navy')\n",
        "plt.title('Total Energy Consumption by Location', fontsize=16, fontweight='bold')\n",
        "plt.xlabel('Charging Station Location', fontsize=12)\n",
        "plt.ylabel('Total Energy Consumed (kWh)', fontsize=12)\n",
        "plt.xticks(rotation=45)\n",
        "plt.grid(axis='y', linestyle='--', alpha=0.7)\n",
        "plt.tight_layout()\n",
        "plt.savefig('location_wise_demand.png')\n",
        "plt.show()"
    ]
    # Clear outputs
    last_cell['outputs'] = []
    last_cell['execution_count'] = None

with open('/Users/agnik/Desktop/genai/GENAI_Midsem_Submission (1).ipynb', 'w') as f:
    json.dump(nb, f, indent=2)

print("Notebook fixed and saved.")
