"""Small training function with an intentionally incomplete implementation."""


def total_memory_gib(cpus: int, memory_per_cpu_gib: int) -> int:
    """Return total requested memory in GiB."""
    if cpus < 1 or memory_per_cpu_gib < 1:
        raise ValueError("CPU and memory values must be positive")
    return cpus * memory_per_cpu_gib
