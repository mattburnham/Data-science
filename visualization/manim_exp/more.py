from manim import *


class MovingFrame(Scene):
	def construct(self):
		# Write equations
		equation = MathTex("2x^2-5x+2", "=", "(x-2)(2x-1)")

		# Create animation
		self.play(Write(equation))

		# Add moving frames
		framebox1 = SurroundingRectangle(equation[0], buff=0.1)
		framebox2 = SurroundingRectangle(equation[2], buff=0.1)

		# Create animations
		self.play(Create(framebox1))  # creating the frame

		self.wait()
		# replace frame 1 with frame 2
		self.play(ReplacementTransform(framebox1, framebox2))

		self.wait()


class MathematicalEquation(Scene):
	def construct(self):
		# Write equations
		equation1 = MathTex("2x^2-5x+2")
		eq_sign_1 = MathTex("=")
		equation2 = MathTex("2x^2-4x-x+2")
		eq_sign_2 = MathTex("=")
		equation3 = MathTex("(x-2)(2x-1)")

		# Put each equation or sign in the appropriate positions
		equation1.next_to(eq_sign_1, LEFT)
		equation2.next_to(eq_sign_1, RIGHT)

		eq_sign_2.shift(DOWN)
		equation3.shift(DOWN)

		# Align bottom equations with the top equations
		eq_sign_2.align_to(eq_sign_1, LEFT)
		equation3.align_to(equation2, LEFT)

		# Group equations and sign
		eq_group = VGroup(equation1, eq_sign_1, equation2, eq_sign_2, equation3)

		# Create animation
		self.play(Write(eq_group))
		self.wait()


class MovingAndZoomingCamera(MovingCameraScene):
	def construct(self):
		# Write equations
		equation = MathTex("2x^2-5x+2", "=", "(x-2)(2x-1)")

		self.add(equation)
		self.play(
			self.camera.frame.animate.move_to(equation[0]).set(
				width=equation[0].width * 2
			)
		)
		self.wait(0.3)
		self.play(
			self.camera.frame.animate.move_to(equation[2]).set(
				width=equation[2].width * 2
			)
		)


class Graph(Scene):
	def construct(self):
		axes = Axes(
			x_range=[-3, 3, 1],
			y_range=[-5, 5, 1],
			x_length=6,
			y_length=6,
		)

		# Add labels
		axes_labels = axes.get_axis_labels(x_label="x", y_label="f(x)")

		# Create function graphs
		graph = axes.plot(lambda x: x**2, color=BLUE)
		graph_label = axes.get_graph_label(graph, label="x^2")

		self.add(axes, axes_labels)
		self.play(Create(graph))
		self.play(Write(graph_label))
		self.wait()


class GroupCircles(Scene):
	def construct(self):
		# Create circles
		circle_green = Circle(color=GREEN)
		circle_blue = Circle(color=BLUE)
		circle_red = Circle(color=RED)

		# Set initial positions
		circle_green.shift(LEFT)
		circle_blue.shift(RIGHT)

		# Create 2 different groups
		gr = VGroup(circle_green, circle_red)
		gr2 = VGroup(circle_blue)
		self.add(gr, gr2)  # add two groups to the scene
		self.wait()

		self.play((gr + gr2).animate.shift(DOWN))  # shift 2 groups down

		self.play(gr.animate.shift(RIGHT))  # move only 1 group
		self.play(gr.animate.shift(UP))

		self.play((gr + gr2).animate.shift(RIGHT))  # shift 2 groups to the right
		self.play(circle_red.animate.shift(RIGHT))
		self.wait()


class RollingCircleTrace(Scene):
	def construct(self):
		# Create circle and dot
		circ = Circle(color=BLUE).shift(4 * LEFT)
		dot = Dot(color=BLUE).move_to(circ.get_start())

		# Group dot and circle
		rolling_circle = VGroup(circ, dot)
		trace = TracedPath(circ.get_start)

		rolling_circle.add_updater(lambda m: m.rotate(-0.3))  # Rotate the circle

		self.add(trace, rolling_circle)  # add trace and rolling circle to the scene

		# Shift the circle to 8*RIGHT
		self.play(rolling_circle.animate.shift(8 * RIGHT), run_time=4, rate_func=linear)


class WriteEquation(Scene):
	def construct(self):
		equation = MathTex(r"e^{i\pi} + 1 = 0")

		self.play(Write(equation))
		self.wait()


class EquationSteps(Scene):
	def construct(self):
		step1 = MathTex(r"2x + 5 = 13")
		step2 = MathTex(r"2x = 8")
		step3 = MathTex(r"x = 4")

		self.play(Write(step1))
		self.wait()
		self.play(Transform(step1, step2))
		self.wait()
		self.play(Transform(step1, step3))
		self.wait()


class MovingCamera(MovingCameraScene):
	def construct(self):
		equation = MathTex(r"\frac{d}{dx}(x^2) = 2x")

		self.play(Write(equation))
		self.wait()

		# Zoom in on the derivative
		self.play(self.camera.frame.animate.scale(0.5).move_to(equation[0]))
		self.wait()


class MoveObjectsTogether(Scene):
	def construct(self):
		square = Square(color=BLUE)
		circle = Circle(color=RED)

		# Group objects
		group = VGroup(square, circle)
		group.arrange(RIGHT, buff=1)

		self.play(Create(group))
		self.wait()

		# Move the entire group
		self.play(group.animate.shift(UP * 2))
		self.wait()


class TracePath(Scene):
	def construct(self):
		dot = Dot(color=RED)

		# Create traced path
		path = TracedPath(dot.get_center, stroke_color=BLUE, stroke_width=4)
		self.add(path, dot)

		# Move the dot in a circular pattern
		self.play(MoveAlongPath(dot, Circle(radius=2)), rate_func=linear, run_time=4)
		self.wait()
