import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, ArrowStyle, FancyArrowPatch

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(7.2, 3.36))
ax.set_xlim(0, 7.2)
ax.set_ylim(0, 3.36)
ax.grid(True, which='both', linestyle='--', linewidth=0.5)  # Adding grid with 1.0 spacing
ax.axis('off')  # No axis for a clean diagram

def create_rectangle(center, width, height, label):
    """Creates a rectangle patch with a label at the center."""
    bottom_left = (center[0] - width / 2, center[1] - height / 2)
    rect = FancyBboxPatch(bottom_left, width, height, boxstyle="square,pad=0.1",
                          ec="black", fc="none", lw=1.5)
    ax.add_patch(rect)
    ax.text(center[0], center[1], label, ha='center', va='center', fontsize=12)

def create_arrow(start, end, text, text_offset, bidirectional=False, headless=False):
    """Creates an arrow patch between two points, with an optional label."""
    if headless:
        style = '-|>'
    else:
        style = ArrowStyle.CurveFilledB(head_length=1.5, head_width=0.8)
    arrow = FancyArrowPatch(start, end, arrowstyle=style, mutation_scale=15, lw=1.5)
    ax.add_patch(arrow)
    if bidirectional:
        arrow = FancyArrowPatch(end, start, arrowstyle=style, mutation_scale=15, lw=1.5)
        ax.add_patch(arrow)
    if text:
        ax.annotate(text, xy=((start[0] + end[0]) / 2, (start[1] + end[1]) / 2),
                    xytext=text_offset, textcoords='offset points', ha='center', va='center', fontsize=10)

# Add the blocks to the diagram
create_rectangle((3.6, 2.68), 2.4, 0.68, 'Neural Network')
create_rectangle((3.6, 0.68), 2.4, 0.68, 'Nanosatellite')

# Add the arrows to the diagram, connecting blocks
create_arrow((2.85, 1.1), (2.85, 2.26), 'Reward', (0, 5), headless=True)
#create_arrow((3.6, 1), (3.6, 0.36), 'reward R_t+1', (-30, -15), headless=True)
create_arrow((4.85,2.25), (4.85, 1.1), 'Action', (0, 5), headless=True)
create_arrow((2.45, 1.1), (2.45, 2.26), 'State', (0, -20), headless=True)
#create_arrow((5.2, 0.68), (6.8, 0.68), 'state S_t+1', (0, 5), headless=True)

# Save the figure
plt.savefig('reward.png', bbox_inches='tight')
plt.show()

