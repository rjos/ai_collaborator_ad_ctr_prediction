import matplotlib.pyplot as plt


def custom_plot(axs): 
    """
    """

    # Remove Spines
    remove_spines(axs)


def remove_spines(axs):
    """
    """

    axs.spines[['right', 'top']].set_visible(False)
