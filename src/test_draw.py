from painter.viewing_pipeline import Pipeline
import geometry as g


pl = Pipeline(viewport=(500,500))
pl.transform.translate(y=0,x=0,z=-5)
pl.transform.rotate_x(20)
pl.transform.rotate_y(45)

pl.draw(g.axis)


pl.show()