public class BankersAlgorithm
{
	int p = 5; // Number of processes
	int r = 3; // Number of resources
//need[i][j]=k implies k instances Rj
// is needed by process Pi
	int need[][] = new int[p][r];
	int [][]max;
	int [][]allocation;
	int []available; // determines the available resources of
	// each type
	int safeSequence[] = new int[p];

	void provideValues()
	{
// P0, P1, P2, P3, P4 are the Process names here
// Allocation Matrix
		allocation = new int[][] { { 0, 0, 1, 2 },
			{ 1, 0, 0, 0 },
			{ 1, 3, 5, 4 },
			{ 0, 6, 3, 2 },
			{ 0, 0, 1, 4 }
		};

// MAX Matrix
		max = new int[][] { { 0, 0, 1, 2 },
			{ 1, 7, 5, 0 },
			{ 2, 3, 5, 6 },
			{ 0, 6, 5, 2 },
			{0, 6, 5, 6 }
		};

// Available Resources
		available = new int[] { 1, 5, 2, 0 };
	}

	void checkSafety()
	{
		int count = 0;

//flag array to find the already allocated process
		boolean flag[] = new boolean[p];
		for (int i = 0; i < p; i++)
		{
			flag[i] = false;
		}

//work array to store the copy of available resources
		int work[] = new int[r];
		for (int i = 0; i < r; i++)
		{
			work[i] = available[i];
		}

		while (count < p)
		{
			boolean flag1 = false;
			for (int i = 0; i < p; i++)
			{
				if (flag[i] == false)
				{
					int j;
					for (j = 0; j < r; j++)
					{
						if (need[i][j] > work[j])
							break;
					}
					if (j == r)
					{
						safeSequence[count++] = i;
						flag[i] = true;
						flag1 = true;

						for (j = 0; j < r; j++)
						{
							work[j] = work[j] + allocation[i][j];
						}
					}
				}
			}
			if (flag1 == false)
			{
				break;
			}
		}
		if (count < p)
		{
			System.out.println("The System is UnSafe!");
		}
		else
		{
			System.out.println(" The SAFE Sequence is: ");
			for (int i = 0; i < p; i++)
			{
				System.out.print("P" + safeSequence[i]);
				if (i != p - 1)
					System.out.print(" -> ");
			}
		}
	}

	void getNeed()
	{
		for (int i = 0; i < p; i++)
		{
			for (int j = 0; j < r; j++)
			{
				need[i][j] = max[i][j] - allocation[i][j];
			}
		}
	}

	public static void main(String[] args)
	{

		BankersAlgorithm ba = new BankersAlgorithm();

		ba.provideValues();

		ba.getNeed();

		ba.checkSafety();
	}
}