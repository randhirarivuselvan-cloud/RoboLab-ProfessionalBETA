def validate_cross_stage(project):
    issues = []
    pins = [x for x in project.pin_map if isinstance(x, dict)]
    seen = {}
    for item in pins:
        pin = item.get("pin")
        signal = item.get("signal")
        if pin is not None:
            if pin in seen and seen[pin] != signal:
                issues.append(
                    f"Pin conflict: {pin} maps to both {seen[pin]} and {signal}."
                )
            seen[pin] = signal

    refs = project.firmware.get("referenced_pins", []) if isinstance(project.firmware, dict) else []
    canonical = {
        x.get("signal"): x.get("pin")
        for x in pins
        if isinstance(x, dict)
    }
    for ref in refs:
        if not isinstance(ref, dict):
            continue
        signal = ref.get("signal")
        firmware_pin = ref.get("pin")
        if signal in canonical and firmware_pin != canonical[signal]:
            issues.append(
                f"Firmware/circuit mismatch for {signal}: "
                f"circuit={canonical[signal]}, firmware={firmware_pin}."
            )
    return issues
