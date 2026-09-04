// Self-contained, read-only DOM check, usable by the smoke runner or browser QA.
export function inspectPortraitFrames() {
  const issues = [];
  const number = (value) => Number.parseFloat(value) || 0;
  const radius = (value, width, height) => {
    const parts = (value || '0').split(/\s+/);
    return [width, height].map((size, axis) => {
      const part = parts[axis] || parts[0];
      return number(part) * (part.endsWith('%') ? size / 100 : 1);
    });
  };
  const corners = [
    ['borderTopLeftRadius', 'borderLeftWidth', 'borderTopWidth'],
    ['borderTopRightRadius', 'borderRightWidth', 'borderTopWidth'],
    ['borderBottomRightRadius', 'borderRightWidth', 'borderBottomWidth'],
    ['borderBottomLeftRadius', 'borderLeftWidth', 'borderBottomWidth'],
  ];
  for (const frame of document.querySelectorAll('picture, [class*="portrait"], [class*="avatar"]')) {
    const img = frame.querySelector(':scope > img');
    if (!img) continue;
    const style = getComputedStyle(frame);
    const imageStyle = getComputedStyle(img);
    const box = frame.getBoundingClientRect();
    const imageBox = img.getBoundingClientRect();
    if (box.width < 2 || box.height < 2 || style.visibility === 'hidden' || imageStyle.visibility === 'hidden' || number(style.opacity) === 0 || number(imageStyle.opacity) === 0) continue;
    if (!['hidden', 'clip'].includes(style.overflowX) || !['hidden', 'clip'].includes(style.overflowY)) continue;
    // Padded portraits may intentionally use a separate image shape.
    const inset = [
      imageBox.left - box.left - number(style.borderLeftWidth),
      imageBox.top - box.top - number(style.borderTopWidth),
      box.right - imageBox.right - number(style.borderRightWidth),
      box.bottom - imageBox.bottom - number(style.borderBottomWidth),
    ];
    if (inset.some((gap) => Math.abs(gap) > 2)) continue;
    for (const [corner, horizontalBorder, verticalBorder] of corners) {
      const outer = radius(style[corner], box.width, box.height);
      const inner = radius(imageStyle[corner], imageBox.width, imageBox.height);
      const expected = [
        Math.max(0, outer[0] - number(style[horizontalBorder])),
        Math.max(0, outer[1] - number(style[verticalBorder])),
      ];
      if (inner.some((value, axis) => value > expected[axis] + 0.5)) {
        issues.push({
          frame: `${frame.tagName.toLowerCase()}.${[...frame.classList].join('.')}`,
          corner,
          frameRadius: style[corner],
          imageRadius: imageStyle[corner],
          reason: 'Image rounding exposes the background inside the clipped frame',
        });
      }
    }
  }
  return issues;
}
