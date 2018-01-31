import numpy as np

# Setup
# Equilateral triangle
# Equations derived from https://www.space-electronics.com/contentAssets/Literature/Measuring_W_and_3CG_motor.pdf
# +x is to the right of center of triangle, parallel to line connecting holes 3 to 2
# +y is straight toward hole 1 from the center of the triangle
# +z is upwards from the center of the triangle
hole_to_hole_length = 15  # cm
riser_block_height = 2  # cm

# Scales 1, 2, 3 (CCW with 1 at front of piece)
# Tare with plate and cones resting on scales
m1_1 = 150  # g
m2_1 = 120  # g
m3_1 = 100  # g

m0_1 = m1_1 + m2_1 + m3_1
print('Total mass = ', m0_1)

incline_angle = np.arcsin(riser_block_height / (hole_to_hole_length / np.sqrt(3)))
center_to_hole = hole_to_hole_length / np.sqrt(3) / 2

xloc = (m3_1 - m2_1) * hole_to_hole_length / (2 * m0_1)
yloc = (m2_1 + m3_1) * (hole_to_hole_length / np.sqrt(3)) / m0_1 - center_to_hole


# Add riser block under cone at 1
# Add riser block on top of plate at 2 and 3 (to maintain same change in mass for all scales)

m1_2 = 100  # g
m2_2 = 160  # g
m3_2 = 120  # g

m0_2 = m1_2 + m2_2 + m3_2

yloc_2 = (m2_2 + m3_2) * (hole_to_hole_length / np.sqrt(3)) / m0_2 - center_to_hole

zloc = (yloc - yloc_2) / np.tan(incline_angle)


print('(x, y, z) = (', xloc, ', ', yloc, ', ', zloc, ')')
